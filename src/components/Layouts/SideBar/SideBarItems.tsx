'use client'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { faChevronDown } from '@fortawesome/free-solid-svg-icons'
import { useAnimate } from 'framer-motion'
import { cn } from '@/utils/tw'
import { useState } from 'react'
import { usePathname } from 'next/navigation'

export type SideBarNavDrawerProps = {
  title: string
  link: string
  items?: {
    name: string
    link: string
  }[]
  icon: React.ReactNode
}

export const SideBarNavDrawer = ({
  title,
  items = [],
  link,
  icon,
}: SideBarNavDrawerProps) => {
  const router = useRouter()
  const [scope, animate] = useAnimate()
  const [isOpen, setIsOpen] = useState<boolean>(false)
  const pathname = usePathname()

  const toggleDrawer = () => {
    if (!isOpen) {
      animate('#drawer', { height: 'auto' }, { duration: 0.3 })
      animate('#chev', { rotate: 180 }, { duration: 0.3 })
    }
    if (isOpen) {
      animate('#drawer', { height: '0' }, { duration: 0.3 })
      animate('#chev', { rotate: 0 }, { duration: 0.3 })
    }
    setIsOpen(!isOpen)
  }

  useEffect(() => {
    if (pathname.includes(link) && !isOpen) {
      toggleDrawer()
    }
    if (!pathname.includes(link) && isOpen) {
      toggleDrawer()
    }
  }, [pathname])

  return (
    <div ref={scope}>
      <div
        className={cn(
          'flex p-3 w-full gap-2 items-center rounded-lg select-none cursor-pointer text-text-muted transition-all ',
          isOpen ? 'bg-primary text-primary-foreground' : ''
        )}
        onClick={() => {
          toggleDrawer()
          router.replace(link)
        }}
      >
        {icon}
        <p>{title}</p>
        <FontAwesomeIcon
          icon={faChevronDown}
          className="ml-auto w-4 h-4"
          id="chev"
        />
      </div>

      {/* drawer */}
      <div
        className="pt-3 px-4 overflow-hidden"
        style={{ height: 0 }}
        id="drawer"
      >
        {items.map((item) => (
          <div
            key={item.link}
            className={cn(
              'border-l-2 px-2 transition-all',
              pathname === item.link ? 'border-primary' : ''
            )}
            onClick={() => {
              router.replace(item.link)
            }}
          >
            <SideBarItem isActive={pathname === item.link} name={item.name} />
          </div>
        ))}
      </div>
    </div>
  )
}

export type SideBarItemProps = {
  name: string
  isActive?: boolean
}

export const SideBarItem = ({ name, isActive = false }: SideBarItemProps) => {
  return (
    <div
      className={cn(
        'flex p-3 w-full gap-2 items-center rounded-lg text-text-muted cursor-pointer transition-colors',
        isActive ? 'bg-primary-accent text-primary' : ''
      )}
    >
      {name}
    </div>
  )
}
